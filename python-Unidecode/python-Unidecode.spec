#
# spec file for package python-Unidecode
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
Name:           python-Unidecode
Version:        1.1.0
Release:        0
Summary:        ASCII transliterations of Unicode text
License:        GPL-2.0-or-later
Group:          Development/Languages/Python
URL:            https://pypi.python.org/pypi/Unidecode
Source:         https://files.pythonhosted.org/packages/source/U/Unidecode/Unidecode-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(preun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
It often happens that you have text data in Unicode, but you need to
represent it in ASCII. For example when integrating with legacy code that
doesn't support Unicode, or for ease of entry of non-Roman names on a US
keyboard, or when constructing ASCII machine identifiers from
human-readable Unicode strings that should still be somewhat intelligible
(a popular example of this is when making an URL slug from an article
title).

In most of these examples you could represent Unicode characters as
"???" or "\\15BA\\15A0\\1610", to mention two extreme cases. But that's
nearly useless to someone who actually wants to read what the text says.

What Unidecode provides is a middle road: function unidecode() takes
Unicode data and tries to represent it in ASCII characters (i.e., the
universally displayable characters between 0x00 and 0x7F), where the
compromises taken when mapping between two character sets are chosen to be
near what a human with a US keyboard would choose.

The quality of resulting ASCII representation varies. For languages of
western origin it should be between perfect and good. On the other hand
transliteration (i.e., conveying, in Roman letters, the pronunciation
expressed by the text in some other writing system) of languages like
Chinese, Japanese or Korean is a very complex issue and this library does
not even attempt to address it. It draws the line at context-free
character-by-character mapping. So a good rule of thumb is that the further
the script you are transliterating is from Latin alphabet, the worse the
transliteration will be.

Note that this module generally produces better results than simply
stripping accents from characters (which can be done in Python with
built-in functions). It is based on hand-tuned character mappings that for
example also contain ASCII approximations for symbols and non-Latin
alphabets.

This is a Python port of Text::Unidecode Perl module by
Sean M. Burke <sburke@cpan.org>.

%prep
%setup -q -n Unidecode-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%python_clone -a %{buildroot}%{_bindir}/unidecode

%check
export LANG=en_US.UTF-8
%python_exec setup.py test

%post
%python_install_alternative unidecode

%preun
%python_uninstall_alternative unidecode

%files %{python_files}
%license LICENSE
%doc ChangeLog README.rst
%{python_sitelib}/*
%python_alternative %{_bindir}/unidecode

%changelog
