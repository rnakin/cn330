import dns.resolver
import ipaddress

def get_ip(domain):
    try:
        # Try to resolve IPv6 (AAAA record)
        answers = dns.resolver.resolve(domain, 'AAAA')
        ipv6 = answers[0].to_text()
        return ipv6
    except dns.resolver.NoAnswer:
        # If no AAAA record, fall back to IPv4 (A record)
        try:
            answers = dns.resolver.resolve(domain, 'A')
            ipv4 = answers[0].to_text()
            return ipv4
        except dns.resolver.NoAnswer:
            return None
    except dns.resolver.NXDOMAIN:
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def is_ip(address):
    try:
        ipaddress.ip_address(address)
        return True
    except:
        return False

