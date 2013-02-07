import unittest

from banter import patch

class TestPatch(unittest.TestCase):
    def test_patch_clean_leaves_simple_patch_unmodified(self):
        result = patch.clean(get_simple_patch())
        self.assertEqual(get_simple_patch(), result)

    def test_patch_clean_removes_b_prefix_for_new_files(self):
        result = patch.clean(get_hg_new_file_patch())
        self.assertEqual(get_hg_new_file_patch(False), result)

    def test_patch_clean_removes_ab_prefix_for_modifed_files(self):
        result = patch.clean(get_hg_modified_file_patch())
        self.assertEqual(get_hg_modified_file_patch(False), result)

    def test_patch_clean_does_not_mangle_inner_patch(self):
        result = patch.clean(get_hg_new_file_patch_containing_patch())
        self.assertEqual(get_hg_new_file_patch_containing_patch(False), result)

    def test_patch_clean_handles_multiple_files(self):
        diff =\
            get_simple_patch() +\
            get_hg_new_file_patch() +\
            get_hg_modified_file_patch()

        expected =\
            get_simple_patch() +\
            get_hg_new_file_patch(False) +\
            get_hg_modified_file_patch(False)

        result = patch.clean(diff)
        self.assertEqual(expected, result)

def get_hg_modified_file_patch(include_prefix=True):
    if include_prefix:
        aprefix = "a/"
        bprefix = "b/"
    else:
        aprefix = bprefix = ""

    return \
        "diff --git a/newfile b/newfile\n" +\
        "--- %snewfile\n" % (aprefix) +\
        "+++ %snewfile\n" % (bprefix) +\
        "@@ -1,1 +1,1 @@\n" +\
        "-hello world\n" +\
        "+hello world 2\n"

def get_hg_new_file_patch(include_prefix=True):
    prefix = "b/" if include_prefix else ""
    return \
        "diff --git a/newfile b/newfile\n" +\
        "new file mode 100644\n" +\
        "--- /dev/null\n" +\
        "+++ %snewfile\n" % (prefix) +\
        "@@ -0,0 +1,1 @@\n" +\
        "+hello world\n"

def get_hg_new_file_patch_containing_patch(include_prefix=True):
    prefix = "b/" if include_prefix else ""
    return \
        "diff --git a/diff b/diff\n" +\
        "new file mode 100644\n" +\
        "--- /dev/null\n" +\
        "+++ %sdiff\n" % (prefix) +\
        "@@ -0,0 +1,6 @@\n" +\
        "+diff --git a/newfile b/newfile\n" +\
        "+--- a/newfile\n" +\
        "++++ b/newfile\n" +\
        "+@@ -1,1 +1,1 @@\n" +\
        "+-hello world\n" +\
        "++hello world\n"

def get_simple_patch():
    return \
        "--- file1	2013-02-07 07:24:49.890300907 -0500\n" +\
        "+++ file2	2013-02-07 07:24:53.908377896 -0500\n" +\
        "@@ -1 +1 @@\n" +\
        "-hello\n" +\
        "+world\n"
