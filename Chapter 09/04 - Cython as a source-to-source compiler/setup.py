import os

from setuptools import setup, Extension

try:
    # cython 소스-대-소스 컴파일은 다음 경우에만 이용할 수 있다
    # Cython을 사용할 수 있으며, 특정한 환경 변수를 이용해서
    # Cython을 이용해 C 소스 코드를 생성한다고
    # 명시적으로 지정해야 한다.
    import Cython
    USE_CYTHON = bool(os.environ.get("USE_CYTHON"))

except ImportError:
    USE_CYTHON = False

ext = ".pyx" if USE_CYTHON else ".c"

extensions = [Extension("fibonacci", ["fibonacci" + ext])]

if USE_CYTHON:
    from Cython.Build import cythonize

    extensions = cythonize(extensions)

setup(
    name="fibonacci",
    ext_modules=extensions,
    extras_require={
        # 패키지를 `[with-cython]` 추가 피처와 함께 설치하게 된다면,
        # Cython은 해당 해키지 버전을 설치해야 한다.
        "with-cython": ["cython==0.23.4"]
    },
)
