#
# spec file for package python-emoji
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2018 Matthias Bach <marix@marix.org>.
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
Name:           python-emoji
Version:        0.5.4
Release:        0
Summary:        Emoji for Python
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/carpedm20/emoji/
Source:         https://files.pythonhosted.org/packages/source/e/emoji/emoji-%{version}.tar.gz
# https://github.com/carpedm20/emoji/pull/118
Patch0:         remove_nose.patch
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
This Python module provides unicode emoji output for strings containing emoji codes.
In addition to the official list defined by the unicode consortium a whole bunch of aliases is defined.

Example:
>> import emoji
>> print(emoji.emojize('Python is :thumbs_up:'))
Python is 👍
>> print(emoji.emojize('Python is :thumbsup:', use_aliases=True))
Python is 👍

%prep
%setup -q -n emoji-%{version}
%patch0 -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}/emoji*

%check
%pytest tests/test_core.py tests/test_unicode_codes.py

%files %{python_files}
%doc CHANGES.md README.rst
%license LICENSE.txt
%{python_sitelib}/*

%changelog
