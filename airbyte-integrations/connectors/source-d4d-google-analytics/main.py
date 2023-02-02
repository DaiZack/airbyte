#
# Copyright (c) 2022 Airbyte, Inc., all rights reserved.
#


import sys

from airbyte_cdk.entrypoint import launch
from source_d4d_google_analytics import SourceD4DGoogleAnalytics

if __name__ == "__main__":
    source = SourceD4DGoogleAnalytics()
    launch(source, sys.argv[1:])
