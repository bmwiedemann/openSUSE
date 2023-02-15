#
# spec file for package patterns-glibc-hwcaps
#
# Copyright (c) 2023 SUSE LLC
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


%bcond_with betatest
Name:           patterns-glibc-hwcaps
Version:        20230201
Release:        0
Summary:        Patterns for opting into hwcaps optimized libraries
License:        MIT
Group:          Metapackages
URL:            https://github.com/openSUSE/patterns
Source0:        %{name}-rpmlintrc
BuildRequires:  patterns-rpm-macros
ExclusiveArch:  x86_64

%description
This is an internal package that is used to create the pattern for glibc
hwcaps. Installation of this package does not make sense.

################################################################################
%package x86_64_v3
%pattern_desktopfunctions
Summary:        Install x86-64-v3 optimized software
Group:          Metapackages
Provides:       pattern() = x86_64_v3
Provides:       pattern-icon() = pattern-generic
Requires:       glibc
Supplements:    modalias(cpu:type%%3Ax86*%%3Afeature%%3A*0080*0089*008C*008D*0093*0094*0096*0097*009B*009C*009D*00C0*0123*0125*0128*)
# typo workaround :/
Provides:       patterns-glibc-hwcaps-x86_64-v3 = %{version}

%description x86_64_v3
This package triggers the installation of x86-64-v3 optimized
glibc HWCAPS overlay packages.

%files x86_64_v3
%dir %{_docdir}/patterns
%{_docdir}/patterns/x86_64_v3.txt

################################################################################

%prep

%build

%install
mkdir -p "%{buildroot}%{_docdir}/patterns"
for i in x86_64_v3; do
	echo "This file marks the pattern $i to be installed." \
		>"%{buildroot}%{_docdir}/patterns/$i.txt"
done

%changelog
