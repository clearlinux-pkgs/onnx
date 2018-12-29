#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : onnx
Version  : 1.3.0
Release  : 10
URL      : https://files.pythonhosted.org/packages/f9/02/03c432628b6985c72f8e5ff35ea6db4bbc691eb0b1c7649d26772bbfa201/onnx-1.3.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/f9/02/03c432628b6985c72f8e5ff35ea6db4bbc691eb0b1c7649d26772bbfa201/onnx-1.3.0.tar.gz
Summary  : Open Neural Network Exchange
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause-LBNL MIT NCSA
Requires: onnx-bin = %{version}-%{release}
Requires: onnx-license = %{version}-%{release}
Requires: onnx-python = %{version}-%{release}
Requires: onnx-python3 = %{version}-%{release}
Requires: numpy
Requires: protobuf
Requires: six
Requires: typing
Requires: typing_extensions
BuildRequires : buildreq-cmake
BuildRequires : buildreq-distutils3
BuildRequires : protobuf-dev
BuildRequires : pybind11-dev
BuildRequires : pytest-runner
BuildRequires : python3-dev
BuildRequires : typing_extensions

%description
<p align="center"><img width="40%" src="docs/ONNX_logo_main.png" /></p>
| Linux | Windows |
|-------|---------|
| [![Build Status](https://travis-ci.org/onnx/onnx.svg?branch=master)](https://travis-ci.org/onnx/onnx) | [![Build status](https://ci.appveyor.com/api/projects/status/lm50cevk2hmrll98/branch/master?svg=true)](https://ci.appveyor.com/project/onnx/onnx) |

%package bin
Summary: bin components for the onnx package.
Group: Binaries
Requires: onnx-license = %{version}-%{release}

%description bin
bin components for the onnx package.


%package license
Summary: license components for the onnx package.
Group: Default

%description license
license components for the onnx package.


%package python
Summary: python components for the onnx package.
Group: Default
Requires: onnx-python3 = %{version}-%{release}

%description python
python components for the onnx package.


%package python3
Summary: python3 components for the onnx package.
Group: Default
Requires: python3-core

%description python3
python3 components for the onnx package.


%prep
%setup -q -n onnx-1.3.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1545942954
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/onnx
cp LICENSE %{buildroot}/usr/share/package-licenses/onnx/LICENSE
cp third_party/benchmark/LICENSE %{buildroot}/usr/share/package-licenses/onnx/third_party_benchmark_LICENSE
cp third_party/pybind11/LICENSE %{buildroot}/usr/share/package-licenses/onnx/third_party_pybind11_LICENSE
cp third_party/pybind11/tools/clang/LICENSE.TXT %{buildroot}/usr/share/package-licenses/onnx/third_party_pybind11_tools_clang_LICENSE.TXT
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/backend-test-tools
/usr/bin/check-model
/usr/bin/check-node

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/onnx/LICENSE
/usr/share/package-licenses/onnx/third_party_benchmark_LICENSE
/usr/share/package-licenses/onnx/third_party_pybind11_LICENSE
/usr/share/package-licenses/onnx/third_party_pybind11_tools_clang_LICENSE.TXT

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
