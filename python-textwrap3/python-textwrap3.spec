#
# spec file for package python-textwrap3
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-textwrap3
Version:        0.9.2
Release:        0
Summary:        Textwrap from Python 3.6 backport (plus a few tweaks)
License:        Python-2.0
Group:          Development/Languages/Python
Url:            https://github.com/jonathaneunice/textwrap3
Source:         https://files.pythonhosted.org/packages/source/t/textwrap3/textwrap3-%{version}.zip
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
# SECTION test requirements
BuildRequires:  %{python_module coverage}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest}
# /SECTION
BuildArch:      noarch

%python_subpackages

%description
Textwrap3 is a compatibility back-port of Python 3.6's textwrap
module that supports Python 2.6 forward. This makes a few new
APIs such as shorten and the max_lines parameter available
in a compatible way to all Python versions typically in current use.

By design, Python 3 sensibilities and expectations rule. Especially when
processing text that includes Unicode characters, textwrap3's results may
differ a bit from those of the textwrap of the underlying Python version
(esp. 2.x). In particular, textwrap3 uses the re.UNICODE flag so that
non-ASCII characters such as accented letters are considered legitimate word
characters.

It also adds one tweak, considering the Unicode em-dash
('\N{EM DASH}' or u'\u2014') identical to the simulated ASCII em-dash
'--'.

%prep
%setup -q -n textwrap3-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitelib}
py.test-%{$python_bin_suffix} --assert=plain
}

%files %{python_files}
%doc CHANGES.yml README.rst
%{python_sitelib}/*

%changelog
