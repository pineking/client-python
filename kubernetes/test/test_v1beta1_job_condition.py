# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.5.1-660c2a2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kubernetes.client
from kubernetes.client.rest import ApiException
from kubernetes.client.models.v1beta1_job_condition import V1beta1JobCondition


class TestV1beta1JobCondition(unittest.TestCase):
    """ V1beta1JobCondition unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testV1beta1JobCondition(self):
        """
        Test V1beta1JobCondition
        """
        model = kubernetes.client.models.v1beta1_job_condition.V1beta1JobCondition()


if __name__ == '__main__':
    unittest.main()
