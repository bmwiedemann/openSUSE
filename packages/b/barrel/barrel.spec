#
# spec file for package barrel
#
# Copyright (c) 2021 SUSE LLC, Nuernberg, Germany.
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

Name:           barrel
Version:        0.1.0
Release:        0
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source:         barrel-%{version}.tar.xz

%if 0%{?fedora_version}
BuildRequires:  boost-devel
BuildRequires:  json-c-devel
BuildRequires:  docbook-style-xsl
%else
BuildRequires:  libboost_headers-devel
BuildRequires:  libboost_test-devel
BuildRequires:  libjson-c-devel
BuildRequires:  docbook-xsl-stylesheets
%endif
BuildRequires:  fdupes
BuildRequires:  libstorage-ng-devel >= 4.4.76
BuildRequires:  libtool
BuildRequires:  libxslt
BuildRequires:  readline-devel

Requires:       libstorage-ng1 >= 4.4.76
Recommends:     %{name}-lang

Summary:        Tool for storage management
Url:            http://github.com/openSUSE/barrel
License:        GPL-2.0-only
Group:          System/Packages

%description
barrel is a command line tool for storage management.

%prep
%setup

%build
export CFLAGS="%{optflags} -DNDEBUG"
export CXXFLAGS="%{optflags} -DNDEBUG"

autoreconf -fvi
%configure \
    --docdir="%{_docdir}/%{name}"
make %{?_smp_mflags}

%check
make %{?_smp_mflags} check VERBOSE=1

%install
%make_install

%fdupes -s %{buildroot}

%find_lang barrel

%files
%defattr(-,root,root)
%{_sbindir}/barrel
%dir %{_sysconfdir}/barrel
%doc %dir %{_docdir}/%{name}
%doc %{_docdir}/%{name}/AUTHORS
%doc %{_mandir}/*/barrel.8*
%license %{_docdir}/%{name}/LICENSE

%package lang
Summary:        Languages for package %{name}
Group:          System/Localization
Supplements:    %{name}
Provides:       %{name}-lang-all = %{version}
BuildArch:      noarch

%description lang
Provides translations to the package %{name}

%files lang -f barrel.lang
%defattr(-,root,root)

%changelog
