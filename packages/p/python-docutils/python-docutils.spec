#
# spec file for package python-docutils
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-docutils%{psuffix}
Version:        0.15.2
Release:        0
Summary:        Python Documentation Utilities
License:        Python-2.0 AND BSD-2-Clause AND GPL-2.0-or-later AND GPL-3.0-or-later AND SUSE-Public-Domain
Group:          Development/Languages/Python
URL:            https://pypi.python.org/pypi/docutils/
Source:         https://files.pythonhosted.org/packages/source/d/docutils/docutils-%{version}.tar.gz
Source99:       python-docutils-rpmlintrc
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module xml}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-xml
Requires(post): update-alternatives
Requires(postun): update-alternatives
Recommends:     python-Pillow
Recommends:     python-Pygments
Recommends:     python-roman
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module Pillow}
BuildRequires:  %{python_module Pygments}
BuildRequires:  %{python_module roman}
%endif
%ifpython3
Provides:       docutils = %{version}
Obsoletes:      docutils < %{version}
%endif
%python_subpackages

%description
Docutils is a modular system for processing documentation into useful formats,
such as HTML, XML, and LaTeX. For input Docutils supports reStructuredText, an
easy-to-read, what-you-see-is-what-you-get plaintext markup syntax.

%prep
%setup -q -n docutils-%{version}
# Remove useless ".py" ending from executables:
for i in tools/rst*; do mv "$i" "${i/.py}"; done
sed -i "s|'tools/\(rst.*\)\.py'|'tools/\1'|" setup.py
# Remove shebang from non-executable files
for i in {'code_analyzer','error_reporting','punctuation_chars','smartquotes','math/latex2mathml','math/math2html','math/tex2mathml_extern'}; do
sed -i -e "1d" "docutils/utils/$i.py"
done
sed -i -e "1d" "docutils/writers/xetex/__init__.py" "docutils/writers/_html_base.py"

%build
%python_build

# test3 is generated from test during build
%if 0%{?have_python2} && ! 0%{?skip_python2}
mv test test%{python2_bin_suffix}
%endif
%if 0%{?have_python3} && ! 0%{?skip_python3}
mv test3 test%{python3_bin_suffix}
%endif

%install
%if !%{with test}
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

# To avoid conflicts with the rst2html4 package
mv %{buildroot}%{_bindir}/rst2html4 %{buildroot}%{_bindir}/rst2html4-docutils
ln -s -f %{_sysconfdir}/alternatives/rst2html4 %{buildroot}%{_bindir}/rst2html4

# To avoid conflicts with the rst2html5 package
mv %{buildroot}%{_bindir}/rst2html5 %{buildroot}%{_bindir}/rst2html5-docutils
ln -s -f %{_sysconfdir}/alternatives/rst2html5 %{buildroot}%{_bindir}/rst2html5
%endif

%ifpython3
%post
update-alternatives --install %{_bindir}/rst2html4 rst2html4 %{_bindir}/rst2html4-docutils 15
update-alternatives --install %{_bindir}/rst2html5 rst2html5 %{_bindir}/rst2html5-docutils 15
%endif

%ifpython3
%postun
if [ ! -f %{_bindir}/rst2html4-docutils ] ; then
   update-alternatives --remove rst2html4 %{_bindir}/rst2html4-docutils
fi
if [ ! -f %{_bindir}/rst2html5-docutils ] ; then
   update-alternatives --remove rst2html5 %{_bindir}/rst2html5-docutils
fi
%endif

%check
%if %{with test}
%python_exec test%{$python_bin_suffix}/alltests.py
%endif

%if !%{with test}
%files %{python_files}
%license COPYING.txt licenses/*.txt
%doc FAQ.txt HISTORY.txt README.txt THANKS.txt BUGS.txt docs/*
%python3_only %{_bindir}/rst2html
%python3_only %{_bindir}/rst2latex
%python3_only %{_bindir}/rst2man
%python3_only %{_bindir}/rst2odt
%python3_only %{_bindir}/rst2odt_prepstyles
%python3_only %{_bindir}/rst2pseudoxml
%python3_only %{_bindir}/rst2s5
%python3_only %{_bindir}/rst2xetex
%python3_only %{_bindir}/rst2xml
%python3_only %{_bindir}/rstpep2html
%python3_only %{_bindir}/rst2html4
%python3_only %{_bindir}/rst2html4-docutils
%python3_only %{_bindir}/rst2html5
%python3_only %{_bindir}/rst2html5-docutils
%python3_only %ghost %{_sysconfdir}/alternatives/rst2html4
%python3_only %ghost %{_sysconfdir}/alternatives/rst2html5
%{python_sitelib}/docutils/
%{python_sitelib}/docutils-%{version}-py%{python_version}.egg-info
%endif

%changelog
