#
# Copyright (c) 2022 Airbyte, Inc., all rights reserved.
#


from setuptools import find_packages, setup

MAIN_REQUIREMENTS = ["airbyte-cdk", "PyJWT", "cryptography", "requests"]

TEST_REQUIREMENTS = [
    "pytest~=6.1",
    "requests-mock",
    "pytest-mock",
    "freezegun",
    "source-acceptance-test",
]

setup(
    name="source_d4d_google_analytics",
    description="Source implementation for D4d Google Analytics.",
    author="Airbyte",
    author_email="contact@airbyte.io",
    packages=find_packages(),
    install_requires=MAIN_REQUIREMENTS,
    package_data={"": ["*.json", "schemas/*.json", "schemas/shared/*.json"]},
    extras_require={
        "tests": TEST_REQUIREMENTS,
    },
)
