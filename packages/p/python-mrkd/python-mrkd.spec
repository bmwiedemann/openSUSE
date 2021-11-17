#
# spec file for package python-mrkd
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python2 1
%define progname mrkd
Name:           python-mrkd
Version:        0.2.0
Release:        0
Summary:        Markdown API
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            https://github.com/refi64/mrkd
Source:         %{name}-%{version}.tar.xz
BuildArch:      noarch
BuildRequires:  %{python_module Jinja2}
BuildRequires:  %{python_module base}
BuildRequires:  %{python_module mistune}
BuildRequires:  %{python_module pygments}
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
%if 0%{?suse_version} && 0%{?suse_version} > 1500
Requires(post): update-alternatives
Requires(postun):update-alternatives
%endif
Requires:       python-Jinja2
Requires:       python-Pygments
Requires:       python-mistune
%python_subpackages

%description
Write man pages using Markdown, and convert them to Roff or HTML.

%prep
%autosetup -p1

sed -i -e '/^#!\//, 1d' %{progname}/__init__.py

%build
%python_build

%install
%python_install
%if 0%{?suse_version} && 0%{?suse_version} > 1500
%python_clone -a %{buildroot}%{_bindir}/%{progname}
%endif

%check
%{python_expand PYTHON=%{buildroot}%{$python_sitelib}
$python -mmrkd -f roff -index test/index.ini test/test.1.md test/test.1.output
cmp test/test.1 test/test.1.output
}

%if 0%{?suse_version} && 0%{?suse_version} > 1500
%post
%python_install_alternative %{progname}

%postun
%python_uninstall_alternative %{progname}
%endif

%files %python_files
%defattr(-,root,root,-)
%if 0%{?suse_version} && 0%{?suse_version} > 1500
%python_alternative %{_bindir}/%{progname}
%else
%attr(755,root,root) %{_bindir}/%{progname}
%endif
%{python_sitelib}/*
%doc README.md
%license LICENSE

%changelog
