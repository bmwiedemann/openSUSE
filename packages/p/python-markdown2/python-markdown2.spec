#
# spec file for package python-markdown2
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-markdown2
Version:        2.3.8
Release:        0
Summary:        A Python implementation of Markdown
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/trentm/python-markdown2
Source:         https://files.pythonhosted.org/packages/source/m/markdown2/markdown2-%{version}.tar.gz
Patch0:         0001-Fix-for-issue-348-incomplete-tags-with-punctuation-a.patch
Patch1:         0002-Fixed-code-highlighting-unit-tests.patch
BuildRequires:  %{python_module pygments}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
Markdown2 is a Python implementation of Markdown.
It closely matches the behaviour of the original
Perl-implemented Markdown.pl. Markdown2 also comes with a number of
extensions (called "extras") for things like syntax coloring, tables,
header-ids.

%prep
%setup -q -n markdown2-%{version}
%patch0 -p1
%patch1 -p1

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/markdown2
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
pushd test
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} $python test.py -- -knownfailure
popd

%post
%python_install_alternative markdown2

%postun
%python_uninstall_alternative markdown2

%files %{python_files}
%license LICENSE.txt
%doc CHANGES.md CONTRIBUTORS.txt TODO.txt
%python_alternative %{_bindir}/markdown2
%{python_sitelib}/*

%changelog
