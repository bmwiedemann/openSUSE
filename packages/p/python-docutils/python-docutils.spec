#
# spec file for package python-docutils
#
# Copyright (c) 2025 SUSE LLC
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


%{?sle15_python_module_pythons}
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif

%if 0%{?suse_version} > 1500
%bcond_without libalternatives
%else
%bcond_with libalternatives
%endif

Name:           python-docutils%{psuffix}
Version:        0.21.2
Release:        0
Summary:        Python Documentation Utilities
License:        BSD-2-Clause AND Python-2.0 AND GPL-2.0-or-later AND GPL-3.0-or-later AND SUSE-Public-Domain
URL:            https://pypi.python.org/pypi/docutils/
Source:         https://files.pythonhosted.org/packages/source/d/docutils/docutils-%{version}.tar.gz
Source99:       python-docutils-rpmlintrc
BuildRequires:  %{python_module base >= 3.9}
BuildRequires:  %{python_module flit-core}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%if %{with libalternatives}
Requires:       alts
BuildRequires:  alts
%else
Requires(pre):  update-alternatives
Requires(post): update-alternatives
Requires(postun): update-alternatives
%endif
Recommends:     python-Pillow
Recommends:     python-Pygments
Recommends:     python-roman
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module docutils = %{version}}
BuildRequires:  %{python_module packaging}
# BuildRequires:  %%{python_module roman}
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
find . -name \*.mp4 -print -exec chmod -x '{}' \;
find . -name \*.swp -delete

# Remove shebang from non-executable files
sed -i '1{/^#!/d}' \
  docutils/__main__.py \
  docutils/parsers/commonmark_wrapper.py \
  docutils/parsers/recommonmark_wrapper.py \
  docutils/utils/error_reporting.py \
  docutils/utils/math/math2html.py \
  docutils/utils/math/tex2unichar.py \
  docutils/utils/smartquotes.py \
  docutils/writers/_html_base.py \
  docutils/writers/odf_odt/prepstyles.py \
  docutils/writers/xetex/__init__.py

%build
%pyproject_wheel

%install
%if !%{with test}
%pyproject_install
for binary in docutils rst2html rst2latex rst2man rst2odt rst2pseudoxml rst2s5 rst2xetex rst2xml rst2html4 rst2html5 ; do
    %python_clone -a %{buildroot}%{_bindir}/$binary
done
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%check
%if %{with test}
%python_exec test/alltests.py -v
%endif

%if !%{with test}
# sometime ago rst2html was the master which would let fail the upgrade with master docutils in post below
%pre
update-alternatives --query rst2html >/dev/null 2>&1 && update-alternatives --quiet --remove-all rst2html ||:
# If libalternatives is used: Removing old update-alternatives entries.
%python_libalternatives_reset_alternative docutils

%post
%python_install_alternative docutils rst2html rst2latex rst2man rst2odt rst2pseudoxml rst2s5 rst2xetex rst2xml rst2html4 rst2html5

%postun
%python_uninstall_alternative docutils

%files %{python_files}
%license COPYING.txt licenses/*.txt
%doc FAQ.txt HISTORY.txt README.txt THANKS.txt BUGS.txt docs/*
%python_alternative %{_bindir}/docutils
%python_alternative %{_bindir}/rst2html
%python_alternative %{_bindir}/rst2latex
%python_alternative %{_bindir}/rst2man
%python_alternative %{_bindir}/rst2odt
%python_alternative %{_bindir}/rst2pseudoxml
%python_alternative %{_bindir}/rst2s5
%python_alternative %{_bindir}/rst2xetex
%python_alternative %{_bindir}/rst2xml
%python_alternative %{_bindir}/rst2html4
%python_alternative %{_bindir}/rst2html5
%{python_sitelib}/docutils/
%{python_sitelib}/docutils-%{version}.dist-info
%endif

%changelog
