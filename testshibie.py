import face_predict
id_max = common.read_max_id("data_user")
print(id_max)
face,id = face_predict.predict()
print(face,id)
if face == 0:
    csbox = QMessageBox(QMessageBox.Warning, self.tr("超时"), self.tr("已超时，请重新选择！"), QMessageBox.NoButton, self)
    csbox.exec_()
    with open('master.txt', 'w+') as f:
        f.write('0')
        f.close()
elif face == 1:
    self.recordsdate = self.recordsdate + 1
    if self.recordsdate >= self.facesdate:
        self.recordsdate=self.facesdate
    hybox = QMessageBox(QMessageBox.Information, self.tr("成功"), self.tr("签到成功！！"), QMessageBox.NoButton, self)
    hybox.exec_()