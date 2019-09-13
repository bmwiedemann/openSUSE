#
# spec file for package python-cluster
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-cluster
Version:        1.4.1.post2
Release:        0
Summary:        Clustering library for python
License:        LGPL-2.0-or-later
Group:          Development/Languages/Python
URL:            https://github.com/exhuma/python-cluster
Source:         https://files.pythonhosted.org/packages/source/c/cluster/cluster-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-matplotlib >= 1.2
Requires:       python-numpy >= 1.2
Requires:       python-scipy >= 0.12
BuildArch:      noarch
%python_subpackages

%description
The python-cluster package allows you to create several groups
(clusters) of objects from a list. It’s meant to be flexible and able
to cluster any object. To ensure this kind of flexibility, you need
not only to supply the list of objects, but also a function that
calculates the similarity between two of those objects. For simple
datatypes, like integers, this can be as simple as a subtraction, but
more complex calculations are possible. Right now, it is possible to
generate the clusters using a hierarchical clustering and the popular
K-Means algorithm. For the hierarchical algorithm there are different
“linkage” (single, complete, average and uclus) methods available.

%prep
%setup -q -n cluster-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%license LICENSE
%{python_sitelib}/*

%changelog
