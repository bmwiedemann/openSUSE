#
# spec file for package libgnomesu
#
# Copyright (c) 2022 SUSE LLC
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


Name:           libgnomesu
Version:        2.0.7
Release:        0
Summary:        GNOME su Library
License:        LGPL-2.1-or-later
Group:          System/GUI/GNOME
URL:            https://github.com/openSUSE/libgnomesu
Source:         %{url}/releases/download/v%{version}/%{name}-%{version}.tar.xz
Source1:        gnomesu-pam.pamd
# Patch: Avoid patches if possible! Update openSUSE upstream instead.

BuildRequires:  fdupes
BuildRequires:  gtk3-devel
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  pam-devel
Requires:       gsettings-desktop-schemas
Requires:       pam
Requires(pre):  permissions
# Ensure that gnomesu always gets installed
Supplements:    (xdg-utils and gnome-session)

%description
Libgnomesu is a library for providing superuser privileges to GNOME
applications. It supports sudo, consolehelper, PAM, and su.

%package -n libgnomesu0
Summary:        GNOME su Library
Group:          System/Libraries
Requires:       %{name} >= %{version}

%description -n libgnomesu0
Libgnomesu is a library for providing superuser privileges to GNOME
applications. It supports sudo, consolehelper, PAM, and su.

%package devel
Summary:        Development files for libgnomesu
Group:          Development/Libraries/GNOME
Requires:       %{name} = %{version}
Requires:       libgnomesu0 = %{version}

%description devel
This package contains all files needed to develop with libgnomesu.

%lang_package

%prep
%autosetup -p1
cp -a %{SOURCE1} pam-backend/gnomesu-pam

%build
export SUID_CFLAGS="-fPIE"
export SUID_LDFLAGS="-pie"
%configure \
	--docdir=%{_docdir}/%{name} \
	--disable-silent-rules \
	--libexecdir=%{_libexecdir}/%{name} \
	--disable-setuid-error
%make_build

%install
mkdir -p %{buildroot}%{_prefix}/lib/%{name}
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
%find_lang libgnomesu-1.0
mkdir -p %{buildroot}%{_docdir}/%{name}
cp doc/api.html doc/libgnomesu.css %{buildroot}%{_docdir}/%{name}
# We want only PAM backend.
rm -f %{buildroot}%{_libexecdir}/%{name}/gnomesu-backend
%if 0%{?suse_version} > 1500
install -d %{buildroot}/%{_pam_vendordir}
mv %{buildroot}%{_sysconfdir}/pam.d/gnomesu-pam %{buildroot}%{_pam_vendordir}
%endif
%fdupes %{buildroot}

%if 0%{?suse_version} > 1500
%pre
# Prepare for migration to /usr/etc; save any old .rpmsave
for i in pam.d/gnomesu-pam ; do
     test -f %{_sysconfdir}/${i}.rpmsave && mv -v %{_sysconfdir}/${i}.rpmsave %{_sysconfdir}/${i}.rpmsave.old ||:
done

%posttrans
# Migration to /usr/etc, restore just created .rpmsave
for i in pam.d/gnomesu-pam ; do
     test -f %{_sysconfdir}/${i}.rpmsave && mv -v %{_sysconfdir}/${i}.rpmsave %{_sysconfdir}/${i} ||:
done
%endif

%post
%set_permissions %{_libexecdir}/%{name}/gnomesu-pam-backend

%verifyscript
%verify_permissions -e %{_libexecdir}/%{name}/gnomesu-pam-backend

%ldconfig_scriptlets -n libgnomesu0

%files
%license COPYING
%{_bindir}/gnomesu
%dir %{_libexecdir}/%{name}
#%%attr (6755,root,root) %%{_prefix}/lib/%%{name}/gnomesu-backend
#%%attr (6755,root,root) %%{_prefix}/lib/%%{name}/gnomesu-pam-backend
# NOTE: Original package has 6755.
# We have only 4755 and for easy and secure profile.
%verify (not mode) %attr (4755,root,root) %{_libexecdir}/%{name}/gnomesu-pam-backend
%if 0%{?suse_version} > 1500
%{_pam_vendordir}/gnomesu-pam
%else
%config %{_sysconfdir}/pam.d/gnomesu-pam
%endif

%files -n libgnomesu0
%{_libdir}/libgnomesu.so.*

%files lang -f libgnomesu-1.0.lang

%files devel
%dir %{_docdir}/%{name}
%doc %{_docdir}/%{name}/api.html
%doc %{_docdir}/%{name}/libgnomesu.css
%{_includedir}/libgnomesu-1.0
%{_libdir}/libgnomesu.so
%{_libdir}/pkgconfig/libgnomesu-1.0.pc

%changelog
