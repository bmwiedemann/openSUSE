MDSFORMANPAGES="kube-apiserver.md kube-controller-manager.md kube-proxy.md kube-scheduler.md kubelet.md"

# remove comments from man pages
for manpage in ${MDSFORMANPAGES}; do
  pos=$(grep -n "<\!-- END MUNGE: UNVERSIONED_WARNING -->" ${manpage} | cut -d':' -f1)
  if [ -n ${pos} ]; then
    sed -i "1,${pos}{/.*/d}" ${manpage}
  fi
done

# for each man page add NAME and SYNOPSIS section
# kube-apiserver
sed -i -s "s/## kube-apiserver/# NAME\nkube-apiserver \- Provides the API for kubernetes orchestration.\n\n# SYNOPSIS\n**kube-apiserver** [OPTIONS]\n/" kube-apiserver.md

cat << 'EOF' >> kube-apiserver.md
# EXAMPLES
```
/usr/bin/kube-apiserver --logtostderr=true --v=0 --etcd_servers=http://127.0.0.1:4001 --insecure_bind_address=127.0.0.1 --insecure_port=8080 --kubelet_port=10250 --service-cluster-ip-range=10.1.1.0/24 --allow_privileged=false
```
EOF
# kube-controller-manager
sed -i -s "s/## kube-controller-manager/# NAME\nkube-controller-manager \- Enforces kubernetes services.\n\n# SYNOPSIS\n**kube-controller-manager** [OPTIONS]\n/" kube-controller-manager.md

cat << 'EOF' >> kube-controller-manager.md
# EXAMPLES
```
/usr/bin/kube-controller-manager --logtostderr=true --v=0 --master=127.0.0.1:8080
```
EOF
# kube-proxy
sed -i -s "s/## kube-proxy/# NAME\nkube-proxy \- Provides network proxy services.\n\n# SYNOPSIS\n**kube-proxy** [OPTIONS]\n/" kube-proxy.md

cat << 'EOF' >> kube-proxy.md
# EXAMPLES
```
/usr/bin/kube-proxy --logtostderr=true --v=0 --master=http://127.0.0.1:8080
```
EOF
# kube-scheduler
sed -i -s "s/## kube-scheduler/# NAME\nkube-scheduler \- Schedules containers on hosts.\n\n# SYNOPSIS\n**kube-scheduler** [OPTIONS]\n/" kube-scheduler.md

cat << 'EOF' >> kube-scheduler.md
# EXAMPLES
```
/usr/bin/kube-scheduler --logtostderr=true --v=0 --master=127.0.0.1:8080
```
EOF
# kubelet
sed -i -s "s/## kubelet/# NAME\nkubelet \- Processes a container manifest so the containers are launched according to how they are described.\n\n# SYNOPSIS\n**kubelet** [OPTIONS]\n/" kubelet.md

cat << 'EOF' >> kubelet.md
# EXAMPLES
```
/usr/bin/kubelet --logtostderr=true --v=0 --api_servers=http://127.0.0.1:8080 --address=127.0.0.1 --port=10250 --hostname_override=127.0.0.1 --allow-privileged=false
```
EOF

# for all man-pages
for md in $MDSFORMANPAGES; do
	# correct section names
	sed -i -s "s/### Synopsis/# DESCRIPTION/" $md
	sed -i -s "s/### Options/# OPTIONS/" $md
	# add header
	sed -i "s/# NAME/% KUBERNETES(1) kubernetes User Manuals\n# NAME/" $md
	# modify list of options
	# options with no value in ""
	sed -i -r 's/(^      )(-[^":][^":]*)(:)(.*)/\*\*\2\*\*\n\t\4\n/' $md
	# option with value in ""
	sed -i -r 's/(^      )(-[^":][^":]*)("[^"]*")(:)(.*)/\*\*\2\3\*\*\n\t\5\n/' $md
	# options in -s, --long
	sed -i -r 's/(^  )(-[a-z], -[^":][^":]*)(:)(.*)/\*\*\2\*\*\n\t\4\n/' $md
	sed -i -r 's/(^  )(-[a-z], -[^":][^":]*)("[^"]*")(:)(.*)/\*\*\2\3\*\*\n\t\5\n/' $md
	# remove ```
	sed -i 's/```//' $md
	# remove all lines starting with ######
	sed -i 's/^######.*//' $md
	# modify footer
	sed -i -r "s/^\[!\[Analytics\].*//" $md
	# md does not contain section => taking 1
	name="${md%.md}"
	go-md2man -in $md -out man/man1/$name.1
done


