#
# spec file for package python-SpeechRecognition
#
# Copyright (c) 2024 SUSE LLC
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


%define justpython python
Name:           python-SpeechRecognition
Version:        3.12.0
Release:        0
Summary:        Library for performing speech recognition, with support for several engines
# Note: The sources include third party code with different licenses.
# We remove all those before building so it's not installed in the
# generated packages.
License:        BSD-3-Clause
URL:            https://github.com/Uberi/speech_recognition#readme
Source:         https://github.com/Uberi/speech_recognition/archive/%{version}.tar.gz
# Remove information about unbundled libraries.
Patch0:         fix-readme.patch
BuildRequires:  %{python_module audioop-lts if %python-base >= 3.13}
BuildRequires:  %{python_module base >= 3.9}
BuildRequires:  %{python_module google-cloud-speech}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module standard-aifc if %python-base >= 3.13}
BuildRequires:  %{python_module typing-extensions}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  flac
BuildRequires:  python-rpm-macros
Requires:       %{justpython}-SpeechRecognition-common-en-US
Requires:       flac
Requires:       python-PyAudio
Requires:       python-google-cloud-speech
Requires:       python-typing-extensions
%if 0%{?python_version_nodots} >= 313
Requires:       python-audioop-lts
Requires:       python-standard-aifc
%endif
Recommends:     python-pocketsphinx-python
BuildArch:      noarch
%python_subpackages

%description
SpeechRecognition Library for performing speech recognition, with support for several engines and APIs, online and offline.

The Speech recognition engine/API supports CMU Sphinx (works offline), Google Speech Recognition,
Google Cloud Speech API, Wit.ai, Microsoft Bing Voice Recognition, Houndify API and
IBM Speech to Text

%package -n python-SpeechRecognition-common-en-US
Summary:        Common files for en-US language model support in python-speech_recognition

%description -n python-SpeechRecognition-common-en-US
SpeechRecognition Library for performing speech recognition, with support for
several engines and APIs, online and offline.

The Speech recognition engine/API supports CMU Sphinx (works offline), Google
Speech Recognition, Google Cloud Speech API, Wit.ai, Microsoft Bing Voice
Recognition, Houndify API and IBM Speech to Text.

This package contains the data for en-US language model to be used by
pocketsphinx from python-SpeechRecognition.

%prep
%autosetup -p1 -n speech_recognition-%{version}

rm -Rf third-party
rm speech_recognition/flac-*
rm LICENSE-FLAC.txt

%build
%pyproject_wheel

%install
%pyproject_install
# Do not ship tests
%python_expand rm -r %{buildroot}%{$python_sitelib}/tests
%python_expand %fdupes %{buildroot}%{$python_sitelib}
mkdir -p %{buildroot}%{_datadir}/speech_recognition
cp -Ra speech_recognition/pocketsphinx-data %{buildroot}%{_datadir}/speech_recognition/
%python_expand rm -Rf %{buildroot}%{$python_sitelib}/speech_recognition/pocketsphinx-data
%python_expand ln -s %{_datadir}/speech_recognition/pocketsphinx-data %{buildroot}%{$python_sitelib}/speech_recognition/

%check
# No internet access for OpenAI or Groq
ignore="--ignore tests/recognizers/test_groq.py --ignore tests/recognizers/test_openai.py"
ignore+=" --ignore tests/test_whisper_recognition.py"
# PocketSphinx is only built for primary Python
%pytest $ignore -k 'not test_sphinx_'

%files %{python_files}
%license LICENSE.txt
%{python_sitelib}/speech_recognition
%{python_sitelib}/SpeechRecognition-%{version}.dist-info
%dir %{_datadir}/speech_recognition/
%dir %{_datadir}/speech_recognition/pocketsphinx-data

%files -n python-SpeechRecognition-common-en-US
%{_datadir}/speech_recognition/pocketsphinx-data/en-US

%changelog
