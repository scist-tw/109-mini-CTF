<?php
if ($file = $_FILES['file']) {
    if ($file['error']) {
        $msg_type = 'danger';
        $msg = 'Unknown error occurred!!';
    } else if ($file['size'] > 25000) {
        $msg_type = 'warning';
        $msg = 'File too large.';
    } else {
        $filename = bin2hex(random_bytes(32));
        move_uploaded_file($file['tmp_name'], 'upload/' . $filename);
        array_push($_SESSION['files'], $filename);
        $msg_type = 'success';
        $msg = "File uploaded at <a href=\"/upload/$filename\">$filename</a>.";
    }
}
?>

<?php if (isset($msg)): ?>
<div class="alert alert-<?= $msg_type ?>" role="alert">
    <?= $msg ?>
</div>
<br>
<? endif; ?>

<form method="POST" enctype="multipart/form-data" class="row align-items-center">
    <div class="col-auto">
        <input type="file" class="form-control" name="file">
    </div>
    <div class="col-auto">
        <button type="submit" class="btn btn-primary">Upload</button>
    </div>
</form>
