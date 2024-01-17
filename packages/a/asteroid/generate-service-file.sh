#!/bin/sh

commit=64869dfe745800f34f1c68248ba2e350dc95a592
shortcommit=$(c=${commit}; echo ${c:0:7})
version=1.2.1+git

echo -n "Creating _service file ..."
cat << EOF > _service
<services>

   <service name="tar_scm" mode="disabled">
     <param name="url">git://github.com/chazomaticus/asteroid.git</param>
     <param name="scm">git</param>
     <param name="version">${version}-${shortcommit}</param>
     <param name="changesgenerate">enable</param>
   </service>

   <service name="recompress" mode="disabled">
     <param name="file">*.tar</param>
     <param name="compression">bz2</param>
   </service>
   <service name="set_version" mode="disabled"/>

</services>
EOF
echo done
