#
# spec file for package kuberlr
#
# Copyright (c) 2020 SUSE LLC
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


Name:           kuberlr
Version:        0.3.1
Release:        0
Summary:        A tool that simplifies the management of multiple versions of kubectl
License:        Apache-2.0
Group:          System/Management
URL:            https://github.com/flavio/kuberlr
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  golang-packaging
BuildRequires:  golang(API) = 1.13
Requires(post): %fillup_prereq
Requires(post): update-alternatives
Requires(postun): update-alternatives
%if 0%{?suse_version} <= 1500
Conflicts:      kubernetes-client
%endif
Provides:       kubernetes-client-provider = %{version}
%{go_nostrip}

%description
kuberlr (kube-ruler) is a simple wrapper for kubectl. Its main purpose is to
make it easy to manage clusters running different versions of kubernetes.

%prep
%setup -q -a1

%build
export TAG="v%{version}"
export CLOSEST_TAG="v%{version}"
%make_build build

%install
export TAG="v%{version}"
export CLOSEST_TAG="v%{version}"
%make_install
install -D -m 0755 ~/go/bin/%{name} "%{buildroot}/%{_bindir}/%{name}"
%if 0%{?suse_version} <= 1500
install -D -m 0644 %{name}.conf.example %{buildroot}/%{_sysconfdir}/%{name}.conf
%else
install -D -m 0644 %{name}.conf.example %{buildroot}/%{_distconfdir}/%{name}.conf
%endif
# update alternatives
ln -s %{_sysconfdir}/alternatives/kubectl %{buildroot}%{_bindir}/kubectl

%post
%{_sbindir}/update-alternatives \
  --install %{_bindir}/kubectl kubectl %{_bindir}/kuberlr 1000

%postun
if [ ! -f %{_bindir}/%{name} ] ; then
  update-alternatives --remove kubectl %{_bindir}/%{name}
fi

%files
%license LICENSE
%doc README.md
%{_bindir}/kubectl
%{_bindir}/%{name}
%ghost %{_sysconfdir}/alternatives/kubectl
%if 0%{?suse_version} <= 1500
%config %{_sysconfdir}/%{name}.conf
%else
%{_distconfdir}/%{name}.conf
%endif

%changelog
