#!/bin/sh

commit=43554b1ae4887791ae7ebd76f57c84ce0296d1cb
shortcommit=$(c=${commit}; echo ${c:0:7})
version=5.31+git

echo -n "Creating _service file ..."
cat << EOF > _service
<services>

  <service name="tar_scm">
    <param name="scm">git</param>
    <param name="url">git://github.com/fladd/py-fishcrypt.git</param>
    <param name="version">${version}-${shortcommit}</param>
    <param name="revision">${commit}</param>
    <param name="package-meta">yes</param>
  </service>

  <service name="recompress">
    <param name="compression">bz2</param>
    <param name="file">*.tar</param>
  </service>

  <service name="download_files" />

</services>
EOF
echo done
