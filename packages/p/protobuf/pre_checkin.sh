#!/bin/sh
cp protobuf.changes protobuf-java.changes
cp protobuf.changes python-protobuf.changes
osc service runall format_spec_file

