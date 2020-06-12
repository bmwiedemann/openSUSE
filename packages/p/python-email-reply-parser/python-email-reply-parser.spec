#
# spec file for package python-email-reply-parser
#
# Copyright (c) 2020 SUSE LINUX GmbH, Nuernberg, Germany.
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-email-reply-parser
Version:        0.5.9
Release:        0
License:        MIT
Summary:        Email reply parser
Url:            https://github.com/zapier/email-reply-parser
Group:          Development/Languages/Python
Source:         https://github.com/zapier/email-reply-parser/archive/v%{version}.tar.gz#/email_reply_parser-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildArch:      noarch

%python_subpackages

%description
Email reply parser.

%prep
%setup -q -n email-reply-parser-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
%python_exec setup.py test

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/*

%changelog
