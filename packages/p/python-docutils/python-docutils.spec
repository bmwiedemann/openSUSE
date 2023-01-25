#
# spec file
#
# Copyright (c) 2023 SUSE LLC
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
Name:           python-docutils%{psuffix}
Version:        0.19
Release:        0
Summary:        Python Documentation Utilities
License:        BSD-2-Clause AND Python-2.0 AND GPL-2.0-or-later AND GPL-3.0-or-later AND SUSE-Public-Domain
URL:            https://pypi.python.org/pypi/docutils/
Source:         https://files.pythonhosted.org/packages/source/d/docutils/docutils-%{version}.tar.gz
Source99:       python-docutils-rpmlintrc
# PATCH-FIX-OPENSUSE pygments-2.14.patch shp#docutils#201
Patch0:         pygments-2.14.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  %{python_module xml}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-xml
Requires(post): update-alternatives
Requires(postun):update-alternatives
Recommends:     python-Pillow
Recommends:     python-Pygments
Requires:       python-packaging
Recommends:     python-roman
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module Pillow}
BuildRequires:  %{python_module Pygments}
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module roman}
%endif
%if "%{python_flavor}" == "python3" || "%{?python_provides}" == "python3"
Provides:       docutils = %{version}
Obsoletes:      docutils < %{version}
%endif
%python_subpackages

%description
Docutils is a modular system for processing documentation into useful formats,
such as HTML, XML, and LaTeX. For input Docutils supports reStructuredText, an
easy-to-read, what-you-see-is-what-you-get plaintext markup syntax.

%prep
%autosetup -p1 -n docutils-%{version}
# Remove useless ".py" ending from executables:
for i in tools/rst*; do mv "$i" "${i/.py}"; done
sed -i "s|'tools/\(rst.*\)\.py'|'tools/\1'|" setup.py
find . -name \*.mp4 -print -exec chmod -x '{}' \;

# Actually seems to work with Python 3.6
sed -i -e '/python_requires/s/7/6/' setup.py

%build
%pyproject_wheel

%install
%if !%{with test}
%pyproject_install
for binary in docutils rst2html rst2latex rst2man rst2odt rst2odt_prepstyles rst2pseudoxml rst2s5 rst2xetex rst2xml rstpep2html rst2html4 rst2html5 ; do
    %python_clone -a %{buildroot}%{_bindir}/$binary
done
%{python_expand %fdupes %{buildroot}%{$python_sitelib}

# Remove shebang from non-executable files
for i in code_analyzer error_reporting punctuation_chars smartquotes math/latex2mathml math/math2html math/tex2mathml_extern ; do
    sed -i -e '1{\@^#! *%{_bindir}.*python@d}' %{buildroot}%{$python_sitelib}/docutils/utils/$i.py
done
for i in writers/xetex/__init__ writers/_html_base __main__ parsers/commonmark_wrapper parsers/recommonmark_wrapper ; do
    sed -i -e '1{\@^#! *%{_bindir}.*python@d}' %{buildroot}%{$python_sitelib}/docutils/$i.py
done
}

%endif

%check
%if %{with test}
%python_exec test/alltests.py -v
%endif

%if !%{with test}
%post
%{python_install_alternative docutils rst2html rst2latex rst2man rst2odt rst2odt_prepstyles rst2pseudoxml rst2s5 rst2xetex rst2xml rstpep2html rst2html4 rst2html5}

%postun
%{python_uninstall_alternative docutils rst2html rst2latex rst2man rst2odt rst2odt_prepstyles rst2pseudoxml rst2s5 rst2xetex rst2xml rstpep2html rst2html4 rst2html5}
%endif

%if !%{with test}
%files %{python_files}
%license COPYING.txt licenses/*.txt
%doc FAQ.txt HISTORY.txt README.txt THANKS.txt BUGS.txt docs/*
%python_alternative %{_bindir}/docutils
%python_alternative %{_bindir}/rst2html
%python_alternative %{_bindir}/rst2latex
%python_alternative %{_bindir}/rst2man
%python_alternative %{_bindir}/rst2odt
%python_alternative %{_bindir}/rst2odt_prepstyles
%python_alternative %{_bindir}/rst2pseudoxml
%python_alternative %{_bindir}/rst2s5
%python_alternative %{_bindir}/rst2xetex
%python_alternative %{_bindir}/rst2xml
%python_alternative %{_bindir}/rstpep2html
%python_alternative %{_bindir}/rst2html4
%python_alternative %{_bindir}/rst2html5
%{python_sitelib}/docutils/
%{python_sitelib}/docutils-%{version}*-info
%endif

%changelog
