#
# spec file for package openSUSE-EULAs
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


%bcond_without  java

Name:           openSUSE-EULAs
Version:        84.87.20200511.4de0f73
Release:        0
URL:            https://github.com/openSUSE/openSUSE-EULAs
Summary:        Collection of EULAs for openSUSE
License:        MIT
Group:          Development/Other
Source:         openSUSE-EULAs-%{version}.tar.xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
Provides:       package-EULAs
%if %{with java}
# we abuse the no java path here to skip license processing in staging
BuildRequires:  translate-toolkit
%endif

%description
openSUSE-EULAs is a collection of the end user license agreements (EULAs) which
govern use of certain (non-free) software. This software is typically packaged
and maintained in the openSUSE NonFree repository.

%prep
%setup -q -n openSUSE-EULAs-%{version}

%build
%if %{with java}
make
%else
# build without translate-toolkit support in staging
make LICENSES=
%endif

%install
%if %{with java}
%make_install
%else
# build without translate-toolkit support in staging
%make_install LICENSES=
%endif

%files
%defattr(-,root,root,-)
%{_defaultdocdir}/eulas

%changelog
