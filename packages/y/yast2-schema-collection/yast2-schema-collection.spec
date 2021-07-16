#
# spec file for package yast2-schema-collection
#
# Copyright (c) 2021 SUSE LLC
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


Name:           yast2-schema-collection
Version:        0.0.1
Release:        0
Summary:        Collection of yast2-schema autoyast XML definitions of released distributions
License:        GPL-2.0-or-later
Group:          System/YaST
Source0:        yast2-schema-collection.tar.xz
Source1:        tarup_yast2_schemas.sh
BuildRequires:  fdupes
BuildRequires:  yast2-devtools
BuildArch:      noarch

%description
Contains a collection of yast2-schema autoyast XML definitions of released distributions.
Those are needed to be able to validate autoyast XML files you might want to use for auto installations

%prep
%setup -q -n %{name}

%build

%install
mkdir -p %{buildroot}%{yast_schemadir}/autoyast/products
cp -a * %{buildroot}%{yast_schemadir}/autoyast/products
%fdupes %{buildroot}

%files
%dir %{yast_schemadir}
%dir %{yast_schemadir}/autoyast/
%dir %{yast_schemadir}/autoyast/products
%{yast_schemadir}/autoyast/products/*

%changelog
