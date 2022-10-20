var webhookUrl = 'PUT YOUR WEBHOOK URL HERE';
var startTag = '<!-- START VEHICLE LISTING -->';
var endTag = '<!-- END VEHICLE LISTING -->';
var urlRegex = new RegExp(/(https?:\/\/[^\s]+)/g);
var titleRegex = new RegExp(/\d\d\d\d\s.*/g);

var listings = findListing(inputData.emailHtml);
var str = findLinks(listings);
postToSlack(str);

function findListing(str) {
	var results = [];

	var listingsWithTail = str.split(startTag);
	listingsWithTail.shift();
	listingsWithTail.forEach(function(item) {
		results.push(item.split(endTag)[0]);
	});

	return results;
}

function findLinks(list) {
	var results = [];

	list.forEach(function(item, index) {
		var links = item.match(urlRegex);
		var title = item.match(titleRegex);
		if (links.length && title) {
			results.push('<' + links[0] + '|' + title + '>');
		}
	});

	return results.join('\r\n');
}

function postToSlack(str) {

	var introText = ':tada: :car: *' + inputData.emailSubject + '*\r\n';

	var body = {
		text: introText + str,
		channel: '#general',
		icon_emoji: ':robot_face:',
		username: 'Autobot'
	};

	fetch(webhookUrl, {
		method: 'POST',
		body: JSON.stringify(body),
		headers: { 'Content-Type': 'application/json' }
	})
	.then(function(data) {
		callback(null, { success: true});
	}).catch(callback)
}