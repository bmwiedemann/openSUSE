#!/bin/sh
name="luasocket"
variants=(
	"lua51"
	"lua53"
)

for variant in ${variants[@]}; do
	cp lua-${name}.changes ${variant}-${name}.changes
	sed \
		-e "s:flavor lua:flavor ${variant}:g" \
		lua-${name}.spec > ${variant}-${name}.spec
done
