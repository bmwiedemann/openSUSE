#
# spec file for package patterns-hpc
#
# Copyright (c) 2024 SUSE LLC
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


Name:           patterns-hpc
Version:        20240315
Release:        0
Summary:        Source Package for HPC Patterns
License:        MIT
Group:          Metapackages
URL:            https://github.com/openSUSE/patterns
Source1:        library-inc.txt
Source2:        devel-inc.txt
Source10:       patterns-hpc-rpmlintrc
BuildRequires:  patterns-rpm-macros
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
ExclusiveArch:  x86_64 aarch64

%description
This is an internal package that is used to create the patterns as part of
the installation source setup.  Installation of this package does not make
sense.
This particular package contains all the HPC related patterns.











################################################################################
%package libraries
%pattern_serverfunctions
Summary:        HPC Modularized Libraries
Group:          Metapackages
Provides:       pattern() = hpc_libraries
Provides:       pattern-icon() = pattern-generic
Provides:       pattern-order() = 2030

Requires:       gnu-compilers-hpc-devel
Requires:       lua-lmod

%include %{SOURCE1}
%include %{SOURCE2}

%description libraries
This package provides all the modularized libraries so that they can be used in an HPC environment. These libraries allow to install several MPI flavors in parallel.
In order to use these libraries one needs to load them via the module command first.

%files libraries
%dir %{_defaultdocdir}/patterns
%{_defaultdocdir}/patterns/patterns-hpc-libraries.txt

%prep

%build

%install

mkdir -p "%{buildroot}%{_defaultdocdir}/patterns"
# loop sis odd, but we might want to add more patterns
for pack in  patterns-hpc-libraries ; do
    echo "This file marks the pattern $pack in version %{version} to be installed." \
		>"%{buildroot}%{_defaultdocdir}/patterns/${pack}.txt"
done

%changelog
