import nfc
import ndef
import time

tags = set()

rec = ndef.UriRecord("https://google.com")


def on_connect(tag):

	tag_id = str(tag).split('ID=')[1]

	if tag_id is None:
		print("Tag cannot be formatted (not supported).")
	elif tag_id is not None:
		print("RFID UI is", tag_id)
		time.sleep(1.5)
	else:
		tag.ndef.records = [rec]


if __name__ == "__main__":
	clf = nfc.ContactlessFrontend()
	if not clf.open('usb'):
		raise RuntimeError("Failed to open NFC device.")

	while True:
		config = {
			'interval': 0.90,
			'on-connect': on_connect
		}
		ret = clf.connect(rdwr=config)
		if ret is None:
			pass
		elif not ret:
			print("NFC connection terminated due to an exception.")
			pass
		else:
			pass
	clf.close()
