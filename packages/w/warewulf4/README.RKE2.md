# RKE2 Cluster Configuration HOWTO

The package warewulf4-overlay-rke2 provides a configuration template
to share a connection token - a shared secret - and the hostname of
the first server endpoint across an RKE2 cluster.  
To use it,

- create a profile `rke2-config-key`:

    ```
	wwctl profile add rke2-config-key
	token="$(printf 'K'; \
         for n in {1..20}; do printf %x $RANDOM; done; \
         printf "::server:"; \
         for n in {1..20}; do printf %x $RANDOM; done)"
	 wwctl profile set --tagadd="connectiontoken=${token}" \
              -O rke2-config rke2-config-key
    ```
- create a profile `rke2-config-first-server`:

	```
    server=<hostname_of_first_rke2_server>
	wwctl profile add rke2-config-first-server
	wwctl profile set --tagadd="server=${server}" -O rke2-config rke2-config-first-server

	```
- add the `rke2-config-key` profile to the server node:

    ```
	wwctl node set -P default,rke2-config-key $server

	```
- finally, add both profiles to the agent nodes:

	```
	agents="<agent_list>"
	wwctl node set -P default,rke2-config-key,rke2-config-first-server $agents
	```

In case the RKE2 server node is not deployed by Warewulf, you will
have to grab the connection token (see variable `token` above) from
the file `/var/lib/rancher/rke2/server/node-token` on the running
server.
