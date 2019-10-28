#!/bin/sh

sed -e 's/^Name:.*erlang-rebar/&-testsuite/' erlang-rebar.spec > erlang-rebar-testsuite.spec
cp erlang-rebar.changes erlang-rebar-testsuite.changes
cp erlang-rebar.rpmlintrc erlang-rebar-testsuite.rpmlintrc
osc service localrun format_spec_file
