#
# spec file for package golang-org-x
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%global provider        github
%global provider_tld    com
%global project         golang
%global repo            tools
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     golang.org/x/tools

Name:           golang-org-x-%{repo}
Version:        1.12+git20190313.aa829657
Release:        0
Summary:        Additional toolsgraphy libraries
License:        BSD-3-Clause
Group:          Development/Languages/Golang
Url:            https://%{provider_prefix}
Source0:        %{repo}-%{version}.tar.xz
Source1:        rpmlintrc
Source2:        godoc.service
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires:  fdupes
BuildRequires:  find
BuildRequires:  golang-packaging
BuildRequires:  systemd
BuildRequires:  xz
%if 0%{?suse_version} > 1500
BuildRequires:  golang(API) >= 1.11
%endif

BuildRequires:  golang-org-x-net-html
Requires:       golang-org-x-net-html
BuildRequires:  golang-org-x-net-websocket
Requires:       golang-org-x-net-websocket
BuildRequires:  golang-org-x-net-context
Requires:       golang-org-x-net-context

%{go_nostrip}
%{go_provides}

%description
This package contains additional toolsgraphy libraries that are developed by the
Go team but outside of the main source tree.

%package -n go-tools
Summary:        Additional toolsgraphy libraries
Group:          Development/Languages/Golang
AutoReqProv:    Off

%{?systemd_requires}
%{go_exclusivearch}

%description -n go-tools
This package contains additional toolsgraphy libraries that are developed by the
Go team but outside of the main source tree.

%prep
%setup -q -n %{repo}-%{version}

rm -rf cover
rm -rf cmd/cover
rm -rf cmd/vet

%build
%goprep %{import_path}
%gobuild ...

%install
%goinstall
%gosrc
%gofilelist

%fdupes %{buildroot}%{_prefix}

install -D -p -m 0644 %{SOURCE2} %{buildroot}%{_unitdir}/godoc.service
install -d %{buildroot}/%{_sbindir}
ln -sf %{_sbindir}/service %{buildroot}%{_sbindir}/rcgodoc

# fix file conflicts with rubygem(bundler),
# which is included in ruby as of ruby2.6
mv %{buildroot}%{_bindir}/bundle %{buildroot}%{_bindir}/go-bundle

%pre -n go-tools
%service_add_pre godoc.service

%post -n go-tools
%service_add_post godoc.service

%preun -n go-tools
%service_del_preun godoc.service

%postun -n go-tools
%service_del_postun godoc.service

%files -f file.lst
%doc README.md AUTHORS CONTRIBUTORS

# /usr/share/licenses is not owned by any package on SLE 12 SP2 and older
%if 0%{?sle_version} <= 120200 && !0%{?is_opensuse}
%doc LICENSE PATENTS
%else
%license LICENSE PATENTS
%endif

%files -n go-tools
%{_bindir}/benchcmp
%{_bindir}/go-bundle
%{_bindir}/callgraph
%{_bindir}/compilebench
%{_bindir}/digraph
%{_bindir}/eg
%{_bindir}/findcall
%{_bindir}/fiximports
%{_bindir}/forward
%{_bindir}/getgo
%{_bindir}/go-contrib-init
%{_bindir}/godex
%{_bindir}/godoc
%{_bindir}/goimports
%{_bindir}/golsp
%{_bindir}/gomvpkg
%{_bindir}/gopackages
%{_bindir}/gopls
%{_bindir}/gorename
%{_bindir}/gotype
%{_bindir}/goyacc
%{_bindir}/guru
%{_bindir}/html2article
%{_bindir}/lostcancel
%{_bindir}/nilness
%{_bindir}/present
%{_bindir}/shadow
%{_bindir}/splitdwarf
%{_bindir}/ssadump
%{_bindir}/stress
%{_bindir}/stringer
%{_bindir}/toolstash
%{_bindir}/unmarshal
%{_bindir}/vet

%{_unitdir}/godoc.service
%{_sbindir}/rcgodoc

%changelog
