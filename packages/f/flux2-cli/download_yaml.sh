#!/bin/bash

for kustomization_file in flux2/manifests/bases/*/kustomization.yaml
do
	echo "$kustomization_file"
	target_dir="$(dirname "$kustomization_file")/"
	echo "target_dir is ${target_dir}"
	while read -r resource
	do
		echo "${resource}"
		rm -f "$(basename "${resource}")"
		wget "${resource}" -O "$(basename "${resource}")"
	done < <(awk '/^- https:\/\/github/ {print $2}' "${kustomization_file}")

	echo "++++++++++++++++"

done
