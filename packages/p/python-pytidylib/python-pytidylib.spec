#
# spec file for package python-pytidylib
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
Name:           python-pytidylib
Version:        0.3.2
Release:        0
Summary:        Python wrapper for HTML Tidy (tidylib) on Python 2 and 3
License:        MIT
Group:          Development/Languages/Python
URL:            http://countergram.com/open-source/pytidylib/
Source:         https://files.pythonhosted.org/packages/source/p/pytidylib/pytidylib-%{version}.tar.gz
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  libtidy-devel
BuildArch:      noarch
%python_subpackages

%description
`PyTidyLib`_ is a Python package that wraps the `HTML Tidy`_ library. This
allows you, from Python code, to "fix" invalid (X)HTML markup. Some of the
library's many capabilities include:

* Clean up unclosed tags and unescaped characters such as ampersands
* Output HTML 4 or XHTML, strict or transitional, and add missing doctypes
* Convert named entities to numeric entities, which can then be used in XML
  documents without an HTML doctype.
* Clean up HTML from programs such as Word (to an extent)
* Indent the output, including proper (i.e. no) indenting for ``pre`` elements,
  which some (X)HTML indenting code overlooks.

Small example of use
====================

The following code cleans up an invalid HTML document and sets an option::

    from tidylib import tidy_document
    document, errors = tidy_document('''<p>f&otilde;o <img src="bar.jpg">''',
      options={'numeric-entities':1})
    print document
    print errors

%prep
%setup -q -n pytidylib-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# The large document test is excluded as it produces inconsistent
# results across architectures.
%pytest -k 'not test_large_document'

%files %{python_files}
%doc README
%license LICENSE
%{python_sitelib}/*

%changelog
