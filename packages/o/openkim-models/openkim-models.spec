#
# spec file for package openkim-models
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2018--2019 Christoph Junghans, Ryan S. Elliott
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


%define         uversion 2019-07-25
Name:           openkim-models
Version:        2019.07.25
Release:        0
Summary:        Open Knowledgebase of Interatomic Models
License:        CDDL-1.0 AND Apache-2.0 AND MPL-2.0 AND GPL-3.0-only AND LGPL-3.0-only
Group:          Productivity/Scientific/Chemistry
URL:            https://openkim.org
Source0:        https://s3.openkim.org/archives/collection/openkim-models-%{uversion}.txz
BuildRequires:  cmake >= 3.4
BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran
BuildRequires:  kim-api-devel >= 2.1.2

%description
OpenKIM is an online framework for making molecular simulations reliable,
reproducible, and portable.  Models conforming to the KIM application
programming interface work seamlessly with major simulation codes that have
adopted the KIM-API standard.

This package contains the models from openkim.org.

%prep
%setup -q -n openkim-models-%{uversion}

%build
%{cmake} ..
%make_jobs

%install
%cmake_install

%files
%defattr(-,root,root,-)
# Each model-driver and model is licensed separately.
# About 2/3 are CDDL-1.0, 1/4 public domain, and 1/12 GPL/LGPL
%license LICENSE
%{_libdir}/kim-api/model-drivers/
%{_libdir}/kim-api/portable-models/
%{_libdir}/kim-api/simulator-models/

%changelog
