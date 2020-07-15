# Postfix container

The command to run this container is:

podman run -d --rm --name postfix -p 25:25 -e SMTP_SERVER=smtp.example.com registry.opensuse.org/opensuse/postfix


## Supported environment variables:
DEBUG=yes|no	enables "set -x" in the entrypoint script
TZ		timezone to use
SERVER_HOSTNAME Server hostname. Emails will appear to come from the
		hostname's domain.
SERVER_DOMAIN   If not set, the domain part of SERVER_HOSTNAME will be used.
SMTP_RELAYHOST	Name of the SMTP relay server to use
SMTP_PORT=587	The relayhost port
SMTP_USERNAME	Username to authenticate with on the relayserver
SMTP_PASSWORD	Password of the SMTP user, alternative SMTP_PASSWORD_FILE
		could be used to point to a file with the password
SMTP_NETWORKS   Comma seperated subnets who are allowed to use the relay.
		E.g. SMTP_NETWORKS='xxx.xxx.xxx.xxx/xx, xxx.xxx.xxx.xxx/xx'
		10.0.0.0/8, 172.16.0.0/12 and 192.168.0.0/16 are preset.
INET_PROTOCOLS	The network interface protocols used for connections.
		Valid values are "all", "ipv4", "ipv6" or "ipv4,ipv6".
		The default value is "ipv4".
MASQUERADE_DOMAINS	Comma separated list of domains that must have their
		subdomain structure stripped off.
MYDESTINATION	List of domains for which mails are delivered locally
		instead of forwarding to another machine.


## Data persistence volumes
/var/spool/postfix	Postfix mail queues. A data volume should be used
			in order to save the queue content if the container
			restarts.
