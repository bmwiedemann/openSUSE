#
# spec file for package python-guessit
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


%define skip_python2 1
Name:           python-guessit
Version:        3.3.1
Release:        0
Summary:        A library for guessing information from video files
License:        LGPL-3.0-only
Group:          Development/Languages/Python
URL:            https://github.com/wackou/guessit
Source0:        https://files.pythonhosted.org/packages/source/g/guessit/guessit-%{version}.tar.gz
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module babelfish >= 0.5.5}
BuildRequires:  %{python_module pytest-benchmark}
BuildRequires:  %{python_module pytest-runner}
BuildRequires:  %{python_module python-dateutil}
BuildRequires:  %{python_module rebulk >= 2.0.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-babelfish >= 0.5.5
Requires:       python-python-dateutil
Requires:       python-rebulk >= 2.0.0
Requires(post): update-alternatives
Requires(postun):update-alternatives
BuildArch:      noarch
%python_subpackages

%description
GuessIt is a Python library that extracts as much information as
possible from a video file.
It has a filename matcher that allows to guess a lot of metadata from
a video using its filename only. This matcher works with both movies
and TV shows episodes.

%prep
%autosetup -n guessit-%{version}
# Remove shebang from non-executable files
for i in {'audio_codec','bit_rate','bonus','cds','container','country','crc','date','edition','episodes','episode_title','film','__init__','language','mimetype','other','part','release_group','screen_size','size','source','streaming_service','title','type','video_codec','website'}; do
  sed -i -e "1d" "guessit/rules/properties/$i.py"
done
for i in {'common/comparators','common/date','common/expected','common/formatters','common/__init__','common/numeral','common/pattern','common/quantity','common/validators','common/words','__init__','markers/groups','markers/__init__','markers/path','processors'}; do
  sed -i -e "1d" "guessit/rules/$i.py"
done
for i in {'api','__init__','jsonutils','__main__','monkeypatch','options','reutils','test/__init__','test/rules/__init__','test/rules/processors_test','test/test_api','test/test_api_unicode_literals','test/test_benchmark','test/test_main','test/test_options','test/test_yml','__version__','yamlutils'}; do
  sed -i -e "1d" "guessit/$i.py"
done

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/guessit
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%post
%python_install_alternative guessit

%postun
%python_uninstall_alternative guessit

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/guessit
%{python_sitelib}/guessit
%{python_sitelib}/guessit-%{version}-py%{python_version}.egg-info

%changelog
