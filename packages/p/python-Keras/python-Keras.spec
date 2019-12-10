#
# spec file for package python-Keras
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


%define srcname keras
%define         skip_python2 1

Name:           python-Keras
Version:        2.3.1
Release:        0
Summary:        Deep Learning library 
License:        MIT
Group:          Development/Languages/Python
Url:            https://github.com/keras-team/keras
Source:         https://github.com/keras-team/keras/archive/%{version}.tar.gz#/%{srcname}-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{pythons}
BuildRequires:  fdupes
BuildRequires:  dos2unix
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Requires:       %{python_module Keras-Applications}
Requires:       %{python_module Keras-Preprocessing}
Requires:       %{python_module PyYAML}
Requires:       %{python_module numpy}
Requires:       %{python_module six}
Requires:       tensorflow
Provides:       python3-keras = %{version}
%python_subpackages

%description
Keras is a high-level neural networks API, written in Python and capable of
running on top of TensorFlow, CNTK, or Theano. It was developed with a focus on
enabling fast experimentation. Being able to go from idea to result with the
least possible delay is key to doing good research.

Use Keras if you need a deep learning library that:

    Allows for easy and fast prototyping (through user friendliness,
    modularity, and extensibility).  Supports both convolutional networks and
    recurrent networks, as well as combinations of the two.  Runs seamlessly on
    CPU and GPU.

Read the documentation at Keras.io.

%package examples
Summary:        High level examples for keras 
Group:          Development/Languages/Python 
Requires:       %{name}

%description examples
This are example scripts for deep learning. Most of the scripts will download
additional contens like traing and test samples.

%prep
%setup -q -n %{srcname}-%{version}

%build
%python_build

%install
%python_install
mkdir -p %{buildroot}/%{_docdir}/%{name}/examples/
install -D examples/* %{buildroot}/%{_docdir}/%{name}/examples
# Keras is used cross platform, so the sources have to be converted
dos2unix %{buildroot}/%{_docdir}/%{name}/examples/class_activation_maps.py \
         %{buildroot}/%{_docdir}/%{name}/examples/mnist_swwae.py \
         %{buildroot}/%{_docdir}/%{name}/examples/neural_doodle.py \

# remove unneeded Keras and doc files
%python_expand rm -r  %{buildroot}%{$python_sitelib}/docs
%python_expand %fdupes %{buildroot}%{$python_sitelib}/keras

%files %{python_files}
%defattr(-,root,root)
%{python_sitelib}/keras
%{python_sitelib}/Keras-*

%files %{python_files examples}
%dir %{_docdir}/%{name}
%{_docdir}/%{name}/examples

%changelog
