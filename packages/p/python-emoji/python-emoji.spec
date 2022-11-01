#
# spec file for package python-emoji
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2021 Matthias Bach <marix@marix.org>
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


Name:           python-emoji
Version:        2.2.0
Release:        0
Summary:        Emoji for Python
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/carpedm20/emoji/
Source:         https://files.pythonhosted.org/packages/source/e/emoji/emoji-%{version}.tar.gz
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

By default, the language is English (``language='en'``) but Spanish (``'es'``), Portuguese (``'pt'``) and Italian (``'it'``) are also supported.

%prep
%autosetup -n emoji-%{version} -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}/emoji*

%check
%pytest

%files %{python_files}
%doc CHANGES.md README.rst
%license LICENSE.txt
%{python_sitelib}/emoji
%{python_sitelib}/emoji-%{version}*-info

%changelog
