# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

class RepositoryResponse(object):

    def __init__(self, message, succeeded):
        self.message = message
        self.succeeded = succeeded