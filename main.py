import dns.resolver
import time
import operator

# Extended list of DNS servers to test
dns_servers = {
    'Google': ['8.8.8.8', '8.8.4.4'],
    'Cloudflare': ['1.1.1.1', '1.0.0.1'],
    'Quad9': ['9.9.9.9', '149.112.112.112'],
    'OpenDNS': ['208.67.222.222', '208.67.220.220'],
    'AdGuard DNS': ['94.140.14.14', '94.140.15.15'],
    'CleanBrowsing': ['185.228.168.9', '185.228.169.9'],
    'Comodo Secure': ['8.26.56.26', '8.20.247.20'],
    'Yandex.DNS': ['77.88.8.8', '77.88.8.1'],
    'Neustar UltraDNS': ['156.154.70.1', '156.154.71.1'],
}

# Domain for testing
test_domain = 'www.wikipedia.org'

results = {}

print(f"Starting DNS test for domain: {test_domain}\n")

for provider, servers in dns_servers.items():
    for server in servers:
        resolver = dns.resolver.Resolver()
        resolver.nameservers = [server]
        resolver.timeout = 2.0
        resolver.lifetime = 2.0
        
        total_time = 0
        num_queries = 3
        successful_queries = 0

        print(f"Testing: {provider.ljust(15)} - {server}")

        for _ in range(num_queries):
            try:
                start_time = time.time()
                resolver.resolve(test_domain, 'A')
                end_time = time.time()
                total_time += (end_time - start_time)
                successful_queries += 1
            except (dns.resolver.NoNameservers, dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.exception.Timeout):
                pass  # Ignore errors and continue

        if successful_queries > 0:
            average_time_ms = (total_time / successful_queries) * 1000  # Convert to milliseconds
            results[f"{provider} ({server})"] = average_time_ms
            print(f"  -> Average time: {average_time_ms:.2f} ms\n")
        else:
            results[f"{provider} ({server})"] = float('inf')
            print("  -> Test failed.\n")

# Sort the results from fastest to slowest
sorted_results = sorted(results.items(), key=operator.itemgetter(1))

print("--- Final Ranking (from fastest to slowest) ---")
for i, (server_info, avg_time) in enumerate(sorted_results, 1):
    if avg_time != float('inf'):
        print(f"{i}. {server_info.ljust(30)} - Average time: {avg_time:.2f} ms")
    else:
        print(f"{i}. {server_info.ljust(30)} - Test failed")
