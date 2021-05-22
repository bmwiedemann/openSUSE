#
# spec file for package golang-github-linuxdeepin-go-x11-client
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

%define   provider        github
%define   provider_tld    com
%define   project         linuxdeepin
%define   repo            go-x11-client
# https://github.com/linuxdeepin/go-x11-client
%define   provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%define   import_path     %{provider_prefix}
# %define   commit          a10a839c0f79ea80d2b4309c6f2d120f98664c5a
# %define   shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           deepin-x11-client
Version:        0.6.3
Release:        0
Summary:        A X11 client Go bindings
License:        GPL-3.0+
URL:            https://github.com/linuxdeepin/go-x11-client
Source0:        https://github.com/linuxdeepin/go-x11-client/archive/%{version}/%{repo}-%{version}.tar.gz
Source1:        vendor.tar.gz
Group:          Development/Languages/Golang
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  libpulse0
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(libcanberra)
BuildRequires:  pkgconfig(libpulse-simple)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pam-devel
BuildRequires:  fdupes
BuildRequires:  mobile-broadband-provider-info
%if 0%{?suse_version} > 1500
BuildRequires:  golang(API) = 1.15
%endif
BuildRequires:  golang-packaging
BuildRequires:  golang(pkg.deepin.io/lib/strv)
BuildRequires:  golang-github-linuxdeepin-go-lib
AutoReqProv:    Off
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{go_provides}
%{go_exclusivearch}

%description
it is a X11 protocol go language binding.

%package -n golang-%{provider}-%{project}-%{repo}
Summary:        Additional golang-github-linuxdeepin-go-x11-client libraries
Group:          Development/Languages/Golang
AutoReqProv:    On
Autoreq:        Off
Requires:       golang(pkg.deepin.io/lib/strv)
Requires:       golang-github-linuxdeepin-go-lib
BuildArch:      noarch

%description -n golang-%{provider}-%{project}-%{repo}
This package contains additional golang-github-linuxdeepin-go-x11-client
libraries that are developed by the Go team but outside of the main source tree.

%prep
%setup -q -a1 -n %{repo}-%{version}

%build
%goprep %{import_path}
%gobuild ...

%install
%goinstall
%gosrc
%gofilelist

%fdupes %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/*

%files -n golang-%{provider}-%{project}-%{repo} -f file.lst
%defattr(-,root,root)
%doc README
%license LICENSE

%changelog
