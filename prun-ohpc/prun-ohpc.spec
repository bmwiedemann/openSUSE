#
# spec file for package prun-ohpc
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           prun-ohpc
Version:        1.0
Release:        0
Summary:        Convenience utility for parallel job launch
License:        BSD-3-Clause
Group:          Productivity/Clustering/Computing
BuildArch:      noarch
Url:            https://github.com/openhpc/ohpc
Source1:        prun
Source2:        LICENSE
Patch1:         prun-Add-user-config.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
prun provides a unified, script-based wrapper for launching parallel jobs
within a resource manager for a variety of MPI families.

%prep
cp %{S:1} %{S:2} .

%patch1 -p0

cat <<EOF > ./prunrc
# Loglvl:  0=error,1=warn,2=info,3=debug
LOGLEVEL=2
EOF

%build

%install
mkdir -p %{buildroot}%{_bindir}
install -D -m 0755 prun %{buildroot}%{_bindir}
install -D -m 0644 prunrc %{buildroot}%{_sysconfdir}/prunrc
install -D -m 0644 prunrc %{buildroot}%{_sysconfdir}/skel/.prunrc

%files
%defattr(-,root,root,-)
%doc LICENSE
%{_bindir}/prun
%config %{_sysconfdir}/prunrc
%config %{_sysconfdir}/skel/.prunrc

%changelog
