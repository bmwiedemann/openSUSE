#
# spec file for package envoy
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


# See also http://en.opensuse.org/openSUSE:Specfile_guidelines
Name:           envoy
Version:        14
Release:        0
Summary:        A ssh/gpg-agent wrapper leveraging cgroups and systemd/socket activation
License:        GPL-3.0+
Group:          System/Management
Url:            https://github.com/vodik/envoy/
Source:         %{name}-%{version}.tar.gz
                # https://github.com/vodik/envoy/archive/v{version}.tar.gz
Patch0:         envoy-fix-new-systemd.patch
BuildRequires:  dbus-1-devel
BuildRequires:  fdupes
BuildRequires:  pam-devel
BuildRequires:  pkg-config
BuildRequires:  ragel
BuildRequires:  systemd-devel
Requires:       openssh
Recommends:     gpg2
%if 0%{?suse_version} >= 1210
BuildRequires:  systemd-rpm-macros
%{?systemd_requires}
%else
Requires:       systemd
%endif

%description
Envoy helps you to manage ssh keys in similar fashion to keychain, but done in
C, takes advantage of cgroups and systemd.

%prep
%setup -q
%patch0 -p1

%build
CFLAGS="%{optflags}" make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot} LIBDIR=/%{_lib}
%fdupes %{buildroot}%{_libexecdir}/systemd

%pre
%service_add_pre envoy@.service envoy@.socket

%post
%service_add_post envoy@.service envoy@.socket

%preun
%service_del_preun envoy@.service envoy@.socket

%postun
%service_del_postun envoy@.service envoy@.socket

%files
%defattr(-,root,root,-)
%doc LICENSE
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_mandir}/*/envoy*
%{_bindir}/envoy
%{_bindir}/envoy-exec
%{_bindir}/envoyd
%{_unitdir}/envoy@.service
%{_unitdir}/envoy@.socket
%{_datadir}/zsh/site-functions/_envoy
%{_libexecdir}/systemd/user/envoy@.service
%{_libexecdir}/systemd/user/envoy@.socket
/%{_lib}/security/pam_envoy.so

%changelog
