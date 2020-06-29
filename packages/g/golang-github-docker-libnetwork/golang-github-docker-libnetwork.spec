#
# spec file for package golang
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
# nodebuginfo


# Handle _multibuild magic.
%define flavour @BUILD_FLAVOR@%{nil}

# We split the Name: into "realname" and "name_suffix".
%define realname golang-%{provider}-%{project}-%{repo}
%if "%flavour" == ""
%define name_suffix %{nil}
%else
%define name_suffix -%{flavour}
%endif

# MANUAL: Update the git_version and git_revision
%define git_version 026aabaa659832804b01754aaadd2c0f420c68b6
%define git_short   026aabaa6598
# git_revision=r$(git rev-list $COMMIT_ID | wc -l)
%define git_revision r2906

%global provider        github
%global provider_tld    com
%global project         docker
%global repo            libnetwork
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     %{provider_prefix}

Name:           %{realname}%{name_suffix}
# NOTE: A while ago, Docker downgraded this dependency on an upgrade, which
#       caused lots of issues when trying to upgrade the RPMs. To fix this, we
#       bumped the version to v0.7.0.1+... which RPM saw as an upgrade.
#       Unfortunately subsequent upgrades have yet to bump the other version
#       components, so we need to keep the '.1' even though it isn't
#       technically correct. Hopefully we will be able to remove it eventually.
Version:        0.7.0.1+git%{git_revision}_%{git_short}
Release:        0
Summary:        Docker Networking
License:        Apache-2.0
Group:          Development/Languages/Golang
URL:            http://github.com/docker/libnetwork
Source0:        %{repo}-git.%{git_short}.tar.xz
Source1:        %{realname}-rpmlintrc
BuildRequires:  fdupes
BuildRequires:  golang-packaging
BuildRequires:  xz
# Due to a limitation in openSUSE's Go packaging we cannot have a BuildRequires
# for 'golang(API) >= 1.13' here, so just require 1.13 exactly. bsc#1172608
BuildRequires:  go1.13
ExcludeArch:    s390
# KUBIC-SPECIFIC: This was required when upgrading from the original kubic
#                 packaging, when everything was renamed to -kubic. It also is
#                 used to ensure that nothing complains too much when using
#                 -kubic packages. Hopfully it can be removed one day.
%if "%flavour" == "kubic"
# Conflict with the non-Kubic package, and provide equivalent
Conflicts:      golang-%{provider}-%{project}-%{repo}
Provides:       golang-%{provider}-%{project}-%{repo} = %{version}
# Disable leap based builds for kubic flavor (bsc#1121412)
%if 0%{?suse_version} == 1500 && 0%{?is_opensuse}
ExclusiveArch:  do_not_build
%endif
%endif
%{go_provides}

%description
Libnetwork provides a native Go implementation for connecting containers

The goal of libnetwork is to deliver a robust Container Network Model that
provides a consistent programming interface and the required network
abstractions for applications.

%package -n docker-libnetwork%{name_suffix}
Summary:        Docker Networking
Group:          System/Management
AutoReqProv:    Off
Conflicts:      docker < 17.09.0_ce
Provides:       fix_bsc_1057743
# We provide a git revision so that Docker can require it properly.
Provides:       docker-libnetwork%{name_suffix}-git = %{git_version}
# KUBIC-SPECIFIC: This was required when upgrading from the original kubic
#                 packaging, when everything was renamed to -kubic. It also is
#                 used to ensure that nothing complains too much when using
#                 -kubic packages. Hopfully it can be removed one day.
%if "%flavour" == "kubic"
# Conflict with non-kubic package, and provide equivalent
Conflicts:      docker-libnetwork-git
Provides:       docker-libnetwork-git = %{version}
%endif

%description -n docker-libnetwork%{name_suffix}
The docker-proxy binary used by Docker that provides Docker with libnetwork
support.


%prep
%setup -q -n %{repo}-git.%{git_short}

%build
%goprep %{import_path}
export CGO_ENABLED=0
%gobuild -buildmode=default cmd/proxy

%install
%{goinstall}
mv %{buildroot}/%{_bindir}/proxy %{buildroot}/%{_bindir}/docker-proxy
%{gosrc}
%{gofilelist}

%fdupes %{buildroot}/%{_prefix}

%files -f file.lst
%defattr(-,root,root,-)
%doc README.md MAINTAINERS
%license LICENSE

%files -n docker-libnetwork%{name_suffix}
%defattr(-,root,root,-)
%{_bindir}/docker-proxy

%changelog
