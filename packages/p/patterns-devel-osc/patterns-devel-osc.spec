#
# spec file for package patterns-devel-osc
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


%bcond_with betatest

Name:           patterns-devel-osc
Version:        20170319
Release:        0
Summary:        Patterns for Installation (osc devel)
License:        MIT
Group:          Metapackages
Url:            https://github.com/openSUSE/patterns
Source0:        %{name}-rpmlintrc
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  patterns-rpm-macros

%description
This is an internal package that is used to create the patterns as part
of the installation source setup.  Installation of this package does
not make sense.

This particular package contains the pattern for building and developing osc.

################################################################################

%package devel_osc_build
%pattern_development
Summary:        Tools for Packaging with Open Build Service
Group:          Metapackages
Provides:       pattern() = devel_osc_build
Provides:       pattern-icon() = pattern-obs-devel
Provides:       pattern-order() = 3280
Provides:       pattern-visible()
Requires:       osc
Requires:       pattern() = basesystem
Recommends:     quilt
Recommends:     spec-cleaner
Recommends:     obs-service-download_files   
Recommends:     obs-service-download_url     
Recommends:     obs-service-extract_file     
Recommends:     obs-service-format_spec_file 
Recommends:     obs-service-recompress       
Recommends:     obs-service-refresh_patches  
Recommends:     obs-service-set_version      
Recommends:     obs-service-source_validator 
Recommends:     obs-service-tar_scm          
Recommends:     obs-service-verify_file      

%description devel_osc_build
Tools for checkouting, patching, building and testing package via osc.

%files devel_osc_build
%dir /usr/share/doc/packages/patterns
/usr/share/doc/packages/patterns/devel_osc_build.txt

################################################################################

%prep

%build

%install
mkdir -p "%{buildroot}/usr/share/doc/packages/patterns"
echo 'This file marks the pattern devel_osc_build to be installed.' >"%{buildroot}/usr/share/doc/packages/patterns/devel_osc_build.txt"

%changelog
