#!/bin/sh -e
osc up
osc rm *.obscpio
osc service disabledrun
version=$(osc diff | sed -n 's/^.*Update to version \([0-9.]\+\):/\1/p')
sed -i -e "s/^\(Version:\s*\)[0-9.]\+/\1$version/g" python-openqa_review.spec
osc add *.obscpio
osc ci -m "Update to $version"
osc sr -m "Update to $version"
