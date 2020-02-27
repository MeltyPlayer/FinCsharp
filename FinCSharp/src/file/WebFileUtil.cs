﻿using System;
using System.Net;

using RSG;

namespace fin.file {
  internal static class WebFileUtil {
    static WebFileUtil() {
      FileUtil.readHandlers.DefineHandler<WebFile>(WebFileUtil.ReadText);
      FileUtil.asyncReadHandlers.DefineHandler<WebFile>(WebFileUtil
        .ReadTextAsync);
    }

    public static string ReadText(WebFile file) {
      using var client = new WebClient();
      return client.DownloadString(new Uri(file.uri));
    }

    public static IPromise<string> ReadTextAsync(WebFile file) {
      var promise = new Promise<string>();
      using (var client = new WebClient()) {
        client.DownloadStringCompleted +=
          (s, ev) => {
            if (ev.Error != null) {
              promise.Reject(ev.Error);
            }
            else {
              promise.Resolve(ev.Result);
            }
          };

        client.DownloadStringAsync(new Uri(file.uri), null);
      }

      return promise;
    }
  }
}